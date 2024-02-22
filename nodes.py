import face_recognition
import numpy as np

class FaceCompareNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": { 
                "image1" : ("IMAGE", {}),
                "image2" : ("IMAGE", {}),
                "process": (["all", "first"],),
             }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("scores",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "calculate_score"
    CATEGORY = "faceCompare"
    
    def calculate_score(self, image1, image2,process):
        result=[]
        for img1 in image1:            
            x=255. * img1.cpu().numpy()
            x=np.clip(x, 0, 255).astype(np.uint8)
            img1_encoding = face_recognition.face_encodings(x)
            if(img1_encoding==[]):
                return (1.0,)
            img1_encoding=img1_encoding[0]
            item=[]
            for img2 in image2:
                y=255. * img2.cpu().numpy()
                y=np.clip(y, 0, 255).astype(np.uint8)
                img2_encoding = face_recognition.face_encodings(y)
                if(img2_encoding==[]):
                    return (1.0,)
                img2_encoding=img2_encoding[0]
                face_distances = face_recognition.face_distance([img1_encoding], img2_encoding)
                item.append(face_distances)
                if(process=="first"):
                    break            
            if(process=="first"):
                result.append(item[0])
                break            
            else:
                result.append(item)        
        print(result)
        return (result,)