import tensorflow as tf
from pathlib import Path
from cnnClassifier.entity.config_entity import EvaluationConfig
from cnnClassifier.utils.common import save_json
from sklearn.metrics import f1_score
import numpy as np


class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    def _valid_generator(self):
        datagenerator_kwargs = dict(rescale=1.0 / 255, validation_split=0.30)

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear",
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs,
        )

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)

    def evaluation(self):
        model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = model.evaluate(self.valid_generator)

        predictions = model.predict(self.valid_generator)
        y_pred = np.argmax(predictions, axis=1)

        # with open("predictions.txt", "w") as f:
        #     for pred in predictions:
        #         f.write(f"{pred}\n")

        # with open("y_pred.txt", "w") as f:
        #     for pred in y_pred:
        #         f.write(f"{pred}\n")

        true_labels = self.valid_generator.labels

        # with open("true_labels.txt", "w") as f:
        #     for label in true_labels:
        #         f.write(f"{label}\n")

        self.f1 = f1_score(true_labels, y_pred)

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1], "f1_score": self.f1}
        save_json(path=Path("scores.json"), data=scores)
