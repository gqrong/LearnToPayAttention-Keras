from LearnToPayAttention import AttentionVGG,AttentionRN
import numpy as np
import scipy.io as sio
from keras.datasets import cifar10
from keras.datasets import cifar100
  
x10 = np.load("datasets/x10.npy")
x100 = np.load("datasets/x100.npy")
y10 = np.load("datasets/y10.npy")
y100 = np.load("datasets/y100.npy")
xsvhn = np.load("datasets/xsvhn.npy") - 1  
ysvhn = np.load("datasets/ysvhn.npy")  
xcub = np.load("datasets/xcub.npy")
ycub = np.load("datasets/ycub.npy")
    
vggatt3concatpcCIFAR10 = AttentionVGG(att='att3', gmode='concat', compatibilityfunction='pc', height=32, width=32, channels=3, outputclasses=10).StandardFit("cifar10",x10,y10)
vggatt3concatpcCIFAR100 = AttentionVGG(att='att3', gmode='concat', compatibilityfunction='pc', height=32, width=32, channels=3, outputclasses=100).StandardFit("cifar100",x100,y100)
vggatt3concatpcSVHN = AttentionVGG(att='att3', gmode='concat', compatibilityfunction='pc', height=32, width=32, channels=3, outputclasses=10).StandardFit("svhn",xsvhn,ysvhn)
vggatt3concatpcCUB = AttentionVGG(att='att3', gmode='concat', compatibilityfunction='pc', height=32, width=32, channels=3, outputclasses=10).StandardFit("cub2002011",xcub,ycub,True)

vggatt2concatpcCIFAR10 = AttentionVGG(att='att2', gmode='concat', compatibilityfunction='pc', height=32, width=32, channels=3, outputclasses=10).StandardFit("cifar10",x10,y10)
vggatt2concatpcCIFAR100 = AttentionVGG(att='att2', gmode='concat', compatibilityfunction='pc', height=32, width=32, channels=3, outputclasses=100).StandardFit("cifar100",x100,y100)
vggatt2concatpcSVHN = AttentionVGG(att='att2', gmode='concat', compatibilityfunction='pc', height=32, width=32, channels=3, outputclasses=10).StandardFit("svhn",xsvhn,ysvhn)
vggatt2concatpcCUB = AttentionVGG(att='att2', gmode='concat', compatibilityfunction='pc', height=32, width=32, channels=3, outputclasses=10).StandardFit("cub2002011",xcub,ycub,True)

RNatt2concatpcCIFAR10 = AttentionRN(att='att2', gmode='concat', compatibilityfunction='pc', height=32, width=32, channels=3, outputclasses=10).StandardFit("cifar10",x10,y10)
RNatt2concatpcCIFAR100 = AttentionRN(att='att2', gmode='concat', compatibilityfunction='pc', height=32, width=32, channels=3, outputclasses=100).StandardFit("cifar100",x100,y100)

vggatt1concatdpCIFAR10 = AttentionVGG(att='att1', gmode='concat', compatibilityfunction='dp', height=32, width=32, channels=3, outputclasses=10).StandardFit("cifar10",x10,y10)
vggatt1concatdpCIFAR100 = AttentionVGG(att='att1', gmode='concat', compatibilityfunction='dp', height=32, width=32, channels=3, outputclasses=100).StandardFit("cifar100",x100,y100)

vggatt1concatpcCIFAR10 = AttentionVGG(att='att1', gmode='concat', compatibilityfunction='pc', height=32, width=32, channels=3, outputclasses=100).StandardFit("cifar10",x10,y10)
vggatt1concatpcCIFAR100 = AttentionVGG(att='att1', gmode='concat', compatibilityfunction='pc', height=32, width=32, channels=3, outputclasses=100).StandardFit("cifar100",x100,y100)

vggatt2indepdpCIFAR10 = AttentionVGG(att='att2', gmode='indep', compatibilityfunction='dp', height=32, width=32, channels=3, outputclasses=10).StandardFit("cifar10",x10,y10)
vggatt2indepdpCIFAR100 = AttentionVGG(att='att2', gmode='indep', compatibilityfunction='dp', height=32, width=32, channels=3, outputclasses=100).StandardFit("cifar100",x100,y100)

vggatt2indeppcCIFAR10 = AttentionVGG(att='att2', gmode='indep', compatibilityfunction='pc', height=32, width=32, channels=3, outputclasses=10).StandardFit("cifar10",x10,y10)
vggatt2indeppcCIFAR100 = AttentionVGG(att='att2', gmode='indep', compatibilityfunction='pc', height=32, width=32, channels=3, outputclasses=100).StandardFit("cifar100",x100,y100)

    
    


