import tensorflow as tf
import tensorflow_datasets as tfds

dataset, info = tfds.load('imdb_reviews', with_info=True, as_supervised=True)
