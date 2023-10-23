from fastapi_utils.cbv import cbv
from fastapi import Form, status
from fastapi_utils.inferring_router import InferringRouter
from apps.utils.standard_response import StandardResponse

# Load API's
router  = InferringRouter()

@cbv(router)
class Testing():
    """This class implements the Texmin API for
    asking questions and gives answers as s3 links."
    """
    @router.get("/process")
    def process_question(self):
        try:
            response = "hello world"
            return response
        except Exception as e:
            return StandardResponse(status=False, 
                                    status_code=status.HTTP_400_BAD_REQUEST,
                                    data=None, message="Invalid")
