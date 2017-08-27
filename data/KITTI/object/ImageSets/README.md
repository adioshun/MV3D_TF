 실행시"ImageSets/train.txt"필요로함
 
 ```python
     def _load_image_set_index(self):
        """
        Load the indexes listed in this dataset's image set file.
        """
        # image_set_file = '$Faster-RCNN_TF/data/KITTI/ImageSets/train.txt'
        image_set_file = os.path.join(self._kitti_path, 'ImageSets',self._image_set + '.txt')
        print("-$$$$ PATH : {}---{}".format(self._kitti_path,self._image_set ))
        assert os.path.exists(image_set_file), \
                'Path does not exist: {}'.format(image_set_file)

        with open(image_set_file) as f:
            image_index = [x.rstrip('\n') for x in f.readlines()]

        print 'image sets length: ', len(image_index)
        print("- image_set_file : {}".format(image_set_file))
        return image_index
  ```
