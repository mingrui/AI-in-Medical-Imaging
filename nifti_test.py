from glob import glob
import SimpleITK

if __name__ == '__main__':
    print("nifti test")
    patients = glob('/media/960EVO/workspace/Data/BRATS-2/Image_Data/HG/**')
    print(patients[0])
    brats2013Image = SimpleITK.ReadImage("/media/960EVO/workspace/Data/BRATS-2/Image_Data/HG/0001/VSD.Brain.XX.O.MR_Flair/VSD.Brain.XX.O.MR_Flair.684.mha")
    brats2015Image = SimpleITK.ReadImage("/media/960EVO/workspace/Data/BRATS2015_Training/HGG/brats_2013_pat0001_1/VSD.Brain.XX.O.MR_Flair.54512/VSD.Brain.XX.O.MR_Flair.54512.mha")
    tiantanImage = SimpleITK.ReadImage("/media/960EVO/TiantanData/IDH_with_respect_to_tiantan_II-III/Moon/HuiyingWan/t2.nii")
    print("brats 2013 image\n")
    print(brats2013Image)
    print("brats 2015 image\n")
    print(brats2015Image)
    print("tiantan image\n")
    print(tiantanImage)
    SimpleITK.Show(brats2013Image, 'brats 2013 image')
    SimpleITK.Show(brats2015Image, 'brats 2015 image')
    SimpleITK.Show(tiantanImage, 'tiantan image')