#include <jni.h>
#include <opencv2/opencv.hpp>

using namespace cv;

extern "C"
JNIEXPORT void JNICALL
Java_com_example_camwra_MainActivity_Canny(JNIEnv *env, jobject thiz,
                                                      jlong mat_addr_input, jlong mat_addr_result,jint th1,jint th2) {
    Mat &matInput = *(Mat *)mat_addr_input;
    Mat &matResult = *(Mat *)mat_addr_result;

    cvtColor(matInput, matResult, COLOR_RGBA2GRAY);
    blur(matInput,matResult,Size(5,5));
    Canny(matInput,matResult,th1,th2);
}


extern "C"
JNIEXPORT void JNICALL
Java_com_example_camwra_MainActivity_Interestedregion(JNIEnv *env, jobject thiz,
                                                      jlong mat_addr_input, jlong mat_addr_result) {
    // TODO: implement Interestedregion()
}