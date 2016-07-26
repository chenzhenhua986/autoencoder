import caffe
class dMRI(caffe.Layer):
  def setup(self, bottom, top):
    shape = (1, 96)
    top[0].reshape(*shape)
  def reshape(self,bottom,top):
    pass
  def forward(self,bottom,top):
    l = open("/l/vision/v5/chen478/autoencoder/train").readlines()
    for i in xrange(0, len(l)):
      tmp = []
      d = l[i].strip('\n')
      tmp.append(d.split(' '))
      top[0].data[...] = tmp
  def backward(self,top,propagate_down,bottom):
      pass

class dMRI_test(caffe.Layer):
  def setup(self, bottom, top):
    shape = (1, 96)
    top[0].reshape(*shape)
  def reshape(self,bottom,top):
    pass
  def forward(self,bottom,top):
    l = open("/l/vision/v5/chen478/autoencoder/test").readlines()
    for i in xrange(0, len(l)):
      tmp = []
      d = l[i].strip('\n')
      tmp.append(d.split(' '))
      top[0].data[...] = tmp
  def backward(self,top,propagate_down,bottom):
      pass
