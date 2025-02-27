import tensorflow as tf
from FaceAging import FaceAging


flags = tf.app.flags
flags.DEFINE_integer(name='epoch', default=50, help='number of epochs')
flags.DEFINE_boolean(name='is_train', default=True, help='training mode')
flags.DEFINE_string(name='dataset', default='UTKFace', help='dataset name')
flags.DEFINE_string(name='savedir', default='save', help='dir for saving training results')
flags.DEFINE_string(name='testdir', default='None', help='dir for testing images')
FLAGS = flags.FLAGS


def main(_):
    print(FLAGS.flag_values_dict())

    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    with tf.Session(config=config) as session:
        model = FaceAging(
            session,  # TensorFlow session
            is_training=FLAGS.is_train,  # flag for training or testing mode
            save_dir=FLAGS.savedir,  # path to save checkpoints, samples, and summary
            dataset_name=FLAGS.dataset  # name of the dataset in the folder ./data
        )
        if FLAGS.is_train:
            print('\n\tTraining Mode')
            model.train(
                num_epochs=FLAGS.epoch,  # number of epochs
            )
        else:
            print('\n\tTesting Mode')
            model.custom_test(
                testing_samples_dir=FLAGS.testdir + '/*jpg'
            )


if __name__ == '__main__':

    tf.app.run()

