# nlp_movierate
**[This code belongs to the "Implementing a CNN for Text Classification in Tensorflow" blog post.](http://www.wildml.com/2015/12/implementing-a-cnn-for-text-classification-in-tensorflow/)**

It is slightly simplified implementation of Kim's [Convolutional Neural Networks for Sentence Classification](http://arxiv.org/abs/1408.5882) paper in Tensorflow.

영화 평점을 textCNN으로 학습시켜, 단어끼리의 연관성을 가지고 작성자의 의도를 파악하는 프로젝트입니다. 총 4가지(강추, 추천, 보통, 비추)로 분류되며 학습 알고리즘은 tensorflow를 이용한 textCNN을 포크하여 사용하였습니다.

![0001](https://user-images.githubusercontent.com/46700478/135394407-7f3eaaf8-878e-40a7-a536-5b7b7b0e4f2d.jpg)
![0002](https://user-images.githubusercontent.com/46700478/135394412-62a93913-0a4b-43e1-9ffe-a166ee33c2da.jpg)
![0003](https://user-images.githubusercontent.com/46700478/135394413-125e3574-441d-4be2-9dd0-b716c421126b.jpg)
![0004](https://user-images.githubusercontent.com/46700478/135394416-f832fea8-017c-41b7-9a76-c78950ec3853.jpg)
![0005](https://user-images.githubusercontent.com/46700478/135394417-22b6f532-8467-44f7-9471-fe9cfbf994d5.jpg)
![0006](https://user-images.githubusercontent.com/46700478/135394418-69fa907a-b953-4b23-aa53-bd5719a93fb6.jpg)
![0007](https://user-images.githubusercontent.com/46700478/135394420-84ea85f3-b206-4018-9fea-9ba5c7c0ef7f.jpg)
![0008](https://user-images.githubusercontent.com/46700478/135394421-eb2c03ce-30f9-47b6-82ea-33833198cdb6.jpg)
![0009](https://user-images.githubusercontent.com/46700478/135394424-70c66b5f-d080-4bb8-a687-d05b294afbca.jpg)
![0010](https://user-images.githubusercontent.com/46700478/135394427-2657a640-54c5-4bbd-af16-71aac7da547e.jpg)
![0011](https://user-images.githubusercontent.com/46700478/135394428-b2ced460-7d92-4a0b-b4c1-025f9e0b079c.jpg)
![0012](https://user-images.githubusercontent.com/46700478/135394430-a24b9c6c-b7c7-4e99-b101-e1fc30b249e6.jpg)
![0013](https://user-images.githubusercontent.com/46700478/135394431-2e50cd9a-3a66-4ae7-bae0-7cd6e8269249.jpg)
![0014](https://user-images.githubusercontent.com/46700478/135394433-b08bdc5d-5913-4247-ad2c-2bf1710b1005.jpg)
![0015](https://user-images.githubusercontent.com/46700478/135394435-b4655d26-4ad3-40f5-ad2e-1d26c99c6018.jpg)
![0016](https://user-images.githubusercontent.com/46700478/135394437-96543cd0-1ba9-4625-b06f-960687214980.jpg)
![0017](https://user-images.githubusercontent.com/46700478/135394439-61b6e888-fb7c-49bc-827c-edcafd0011bb.jpg)
![0018](https://user-images.githubusercontent.com/46700478/135394440-09f4f5ba-d697-40fe-b5c2-556767b0b7a1.jpg)

## Requirements

- Python 3
- Tensorflow > 0.8
- Numpy

## Training

Print parameters:

```bash
./train.py --help
```

```
optional arguments:
  -h, --help            show this help message and exit
  --embedding_dim EMBEDDING_DIM
                        Dimensionality of character embedding (default: 128)
  --filter_sizes FILTER_SIZES
                        Comma-separated filter sizes (default: '3,4,5')
  --num_filters NUM_FILTERS
                        Number of filters per filter size (default: 128)
  --l2_reg_lambda L2_REG_LAMBDA
                        L2 regularizaion lambda (default: 0.0)
  --dropout_keep_prob DROPOUT_KEEP_PROB
                        Dropout keep probability (default: 0.5)
  --batch_size BATCH_SIZE
                        Batch Size (default: 64)
  --num_epochs NUM_EPOCHS
                        Number of training epochs (default: 100)
  --evaluate_every EVALUATE_EVERY
                        Evaluate model on dev set after this many steps
                        (default: 100)
  --checkpoint_every CHECKPOINT_EVERY
                        Save model after this many steps (default: 100)
  --allow_soft_placement ALLOW_SOFT_PLACEMENT
                        Allow device soft device placement
  --noallow_soft_placement
  --log_device_placement LOG_DEVICE_PLACEMENT
                        Log placement of ops on devices
  --nolog_device_placement

```

Train:

```bash
./train.py
```

## Evaluating

```bash
./eval.py
```

## References

- [Convolutional Neural Networks for Sentence Classification](http://arxiv.org/abs/1408.5882)
- [A Sensitivity Analysis of (and Practitioners' Guide to) Convolutional Neural Networks for Sentence Classification](http://arxiv.org/abs/1510.03820)
