#include <jni.h>
#include <opencv2/opencv.hpp>
#ifdef _DEBUG
#define _DEBUG_WAS_DEFINED 1
#undef _DEBUG
#endif

using namespace cv;

extern "C"
JNIEXPORT void JNICALL
Java_com_example_camwra_MainActivity_Canny(JNIEnv *env, jobject thiz,
                                                      jlong mat_addr_input, jlong mat_addr_result,jint th1,jint th2) {
    Mat &matInput = *(Mat *)mat_addr_input;
    Mat &matResult = *(Mat *)mat_addr_result;

    cvtColor(matInput, matResult, COLOR_RGBA2GRAY);
    GaussianBlur(matInput,matResult,Size(5,5),0);
    Canny(matInput,matResult,th1,th2);

}


extern "C"
JNIEXPORT void JNICALL
Java_com_example_camwra_MainActivity_ROI(JNIEnv *env, jobject thiz,
                                                      jlong mat_addr_input, jlong mat_addr_result) {
    Mat &matInput = *(Mat *)mat_addr_input;
    Mat &ROI = *(Mat *)mat_addr_result;
    Rect r(10,10,100,100);
    Mat D=matInput(r);
}