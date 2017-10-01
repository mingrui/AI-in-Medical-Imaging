import nipype.interfaces.fsl as fsl
import nibabel as nib

img = nib.load("t2.nii")
print(img)
img_reorient = nib.load("t2_reorient.nii")
print(img_reorient)

#reorient = fsl.Reorient2Std()
#reorient.inputs.in_file = "t2.nii"
#reorient.inputs.out_file = "t2_reorient.nii"
#res = reorient.run()

# mybet = fsl.BET(in_file='t2.nii', out_file='t2_skull_stripped.nii')
# result = mybet.run()