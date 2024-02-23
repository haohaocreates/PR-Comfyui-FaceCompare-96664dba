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
             },
             "hidden": {
                "unique_id": "UNIQUE_ID",
                "extra_pnginfo": "EXTRA_PNGINFO",
            },
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("scores",)
    OUTPUT_IS_LIST = (True,)
    OUTPUT_NODE = True
    FUNCTION = "calculate_score"
    CATEGORY = "faceCompare"
    
    def calculate_score(self, image1, image2,process,unique_id = None, extra_pnginfo=None):
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
                face_distances = face_recognition.face_distance([img1_encoding], img2_encoding)[0]
                item.append(face_distances)
                if(process=="first"):
                    break            
            if(process=="first"):
                result.append(item[0])
                break            
            else:
                result.append(item)        
        print(result)        
        # print("unique_id:",unique_id)
        # print("extra_pnginfo:",extra_pnginfo)
        # if unique_id and extra_pnginfo:
        #     workflow=extra_pnginfo["workflow"]
        #     node=list((x for x in workflow["nodes"] if str(x["id"])==unique_id))[0]
        #     if node:
        #         print('find node')
        #         node['widgets_values'].append("aaa")
        return {"ui": {"text": str(result)}, "result": (result,)}

NODE_CLASS_MAPPINGS = {
    "FaceCompare": FaceCompareNode,
}