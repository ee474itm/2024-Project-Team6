import os
import numpy as np
from PIL import Image

def apply_mask(image_path, mask_path, result_dir):
    # Open the image and the mask
    image = Image.open(image_path).convert("RGB")
    mask = Image.open(mask_path).convert("L")  # Convert to grayscale

    # Ensure the image and the mask have the same size
    if image.size != mask.size:
        raise ValueError("Image and mask must have the same dimensions")

    image = np.array(image,dtype=np.float64)
    mask = np.array(mask,dtype=np.float64)/255.0
    
    #result = np.zeros_like(image, dtype=np.uint8)
    result = np.zeros((image.shape[0],image.shape[1],image.shape[2]))
    
    #print(image[0][0][0]) #0~255
    #print(mask[0][0]) #0~1
    
    #print("Image dtype:", image.dtype)
    #print("Mask dtype:", mask.dtype)
    #print("Image shape:", image.shape)
    #print("Mask shape:", mask.shape)    

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for k in range(image.shape[2]):
                #if mask[i][j]>=0.8:
                #    result[i][j][k] = image[i][j][k]
                #else:
                #    result[i][j][k] = 255.0
                
                
                cnt=0
                for p in range(-1,2):
                    for q in range(-1,2):
                        if mask[min(max(0,i+p),image.shape[0]-1)][min(max(0,j+q),image.shape[1]-1)]<=0.05:
                            cnt+=1
                if cnt>6:  # To be removed using mask
                    result[i][j][k] = 255.0
                else:
                    result[i][j][k] = image[i][j][k]
    
    result_image = Image.fromarray(result.astype('uint8'),'RGB')

    # Create the result directory if it doesn't exist
    os.makedirs(result_dir, exist_ok=True)
    print(result_dir)

    # Save the result as JPEG in the result directory
    #result_image.save(os.path.join(result_dir, os.path.basename(image_path)))
    result_image.save(os.path.join(result_dir, 'input.jpg'))

if __name__ == "__main__":
    #images must be jpg files
    
    image_path = os.path.join(os.getcwd(), 'test_data', 'test_images')
    mask_path = os.path.join(os.getcwd(), 'test_data', 'u2net_results')
    result_dir = os.path.join(os.getcwd(), 'test_data', 'finalResults')

    # Get the list of image and mask files
    image_files = [f for f in os.listdir(image_path) if f.endswith('.jpg')]
    mask_files = [f for f in os.listdir(mask_path) if f.endswith('.png')]

    i=0
    # Apply mask to each pair of image and mask
    for image_file, mask_file in zip(image_files, mask_files):
        i+=1
        print(i)
        apply_mask(os.path.join(image_path, image_file),os.path.join(mask_path, mask_file),result_dir)
    print("Finish")