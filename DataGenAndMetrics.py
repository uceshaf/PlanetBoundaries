
def train_generator(ids_train_split, batch_size):
    while True:
        for start in range(0, len(ids_train_split), batch_size):
            x_batch = []
            y_batch = []
            end = min(start + batch_size, len(ids_train_split))
            ids_train_batch = ids_train_split[start:end]
            for id in ids_train_batch:
                #print('content/train/tifs/images/'+str(id))
                img = io.imread('train/tifs/images/'+str(id))
                mask = io.imread('train/labels/masks/'+str(id))
                mask = np.expand_dims(mask, axis=2)
                
                x_batch.append(img)
                y_batch.append(mask)
            x_batch = np.array(x_batch, np.float32) / 65535
            y_batch = to_categorical(y_batch)
            #print('Returning from batch')
            yield x_batch, y_batch
            
            
def test_generator(ids_test_split, batch_size):
    while True:
        for start in range(0, len(ids_test_split), batch_size):
            x_batch = []
            y_batch = []
            end = min(start + batch_size, len(ids_test_split))
            ids_test_batch = ids_test_split[start:end]
            for id in ids_test_batch:
                img = io.imread('test/tifs/images/'+str(id))
                mask = io.imread('test/labels/masks/'+str(id))
                mask = np.expand_dims(mask, axis=2)
                
                x_batch.append(img)
                y_batch.append(mask)
            x_batch = np.array(x_batch, np.float32) / 65535
            y_batch = to_categorical(y_batch)
            yield x_batch, y_batch
            
def val_generator(ids_val_split, batch_size):
    while True:
        for start in range(0, len(ids_val_split), batch_size):
            x_batch = []
            y_batch = []
            end = min(start + batch_size, len(ids_val_split))
            ids_val_batch = ids_val_split[start:end]
            for id in ids_val_batch:
                img = io.imread('val/tifs/images/'+str(id))
                mask = io.imread('val/labels/masks/'+str(id))
                mask = np.expand_dims(mask, axis=2)
                x_batch.append(img)
                y_batch.append(mask)
            x_batch = np.array(x_batch, np.float32) / 65535
            y_batch = to_categorical(y_batch)
            yield x_batch, y_batch
            

def recall_m(y_true, y_pred):
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
        recall = true_positives / (possible_positives + K.epsilon())
        return recall

def precision_m(y_true, y_pred):
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
        precision = true_positives / (predicted_positives + K.epsilon())
        return precision

def f1_m(y_true, y_pred):
    precision = precision_m(y_true, y_pred)
    recall = recall_m(y_true, y_pred)
    return 2*((precision*recall)/(precision+recall+K.epsilon()))  
