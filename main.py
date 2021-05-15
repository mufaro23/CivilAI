import os

#Show the number of the data in the test folder
test_data = os.listdir('./data/test')

#Show the number of the data in the train/crack_imgs folder
cracked_imgs = os.listdir('./data/train/crack_imgs')

#Show the numbe of the data in the train/noncrack_imgs folder
noncracked_imgs = os.listdir('./data/train/noncrack_imgs')

print('# of train cracked images: {}'.format(len(cracked_imgs)))
print('# of train non-cracked images: {}'.format(len(noncracked_imgs)))
print('# of test images: {}'.format(len(test_data)))