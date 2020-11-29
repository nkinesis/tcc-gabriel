# 5 create model and compile it
class PrintLogs(tf.keras.callbacks.Callback):

    def on_train_batch_begin(self, batch, logs=None):
        print("\nProcessing batch " + str(batch))
        n_layers = len(self.model.layers)
        last = n_layers-1
        xl = 6
        dl = self.model.layers[xl]
        #print(dl.output)
        x = K.function(self.model.input, dl.output)
        print(x([2, 1637]))
        
    def on_epoch_end(self, epoch, logs=None):
        print()
        print('=======')
        print("Ended epoch " + str(epoch))
        n_layers = len(self.model.layers)
        last = n_layers-1
        xl = 6
        dl = self.model.layers[xl]
        print(dl.output)
        exit()
