import numpy as np
import argparse

DATA_DIR = '../data/'

def main(figureName, classID):
    all_descriptors = np.load(DATA_DIR+'descriptors.npy',allow_pickle=True)
    
    try:
        name = figureName.split('/')[-1].split('.')[0]
        new_figure = np.load(DATA_DIR+'%s.npy'%name)
    
    except IOError:
        print "no descriptor file: %s.npy"%name
        return

    all_descriptors = all_descriptors.tolist()
    all_descriptors.append([new_figure, classID])
    all_descriptors = np.array(all_descriptors)

    np.save(DATA_DIR+'descriptors.npy', all_descriptors)

    print "classify [%s] to class %d"%(figureName, classID)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', action='store', dest='figure_name',
            help='Stick figure name')

    parser.add_argument('-n', action='store', dest='class_id', 
            type=int,
            help='Class ID')

    results = parser.parse_args()
    main(results.figure_name, results.class_id)