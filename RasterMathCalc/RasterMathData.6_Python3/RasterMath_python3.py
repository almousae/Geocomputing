from osgeo import gdal
import numpy
import matplotlib.pyplot as plt

#read raster data; you might need to change the directory if the path is different
dataset =gdal.Open('landsat\L71026029_02920000609_B30_CLIP.TIF',gdal.GA_ReadOnly)
dataset =gdal.Open('landsat\L71026029_02920000609_B40_CLIP.TIF',gdal.GA_ReadOnly)

#read Raster data as two-dimensional array (think like a list)
array=dataset.ReadAsArray()
#array[array<0]=0
print ('cols: ',dataset.RasterXSize, 'rows: ',dataset.RasterYSize)

##access to cells/pixels
##creat a subset because of the 32bit computer memory limit
subset=array[0:500,0:500] #slicing the two-dimension array

ndvi_array = array #make a copy of existing array

meanVal = numpy.mean(subset)
print ('meanVal:',meanVal)

for row in range(0,500): #change to (dataset.RasterYSize) if memory is large
    for col in range(0,500): #change to (dataset.RasterXSize) if memory is large
        subset[row,col] = 2*subset[row,col] #note the subscript order
        ndvi_array[row,col] #NIR[row,col], Red[row,col] #use for calculation


#convert array back into roster image. function in other file

##Alternatively, raster band math
#subset=subset * 2

meanVal = numpy.mean(subset)
print ('new meanVal:',meanVal)

##visualize the data using pyplot
plt.figure()
plt.contourf(subset)  #draw the DEM subset as polygons
plt.contour(subset,20,colors='grey') #draw the contour lines into 20 levels
plt.show()
