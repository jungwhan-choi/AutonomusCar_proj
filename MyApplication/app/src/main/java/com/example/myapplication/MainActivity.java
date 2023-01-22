package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

public class MainActivity extends AppCompatActivity {
    TextView tv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        tv=(TextView)findViewById(R.id.text_view);
        if(!Python.isStarted()){
            Python.start(new AndroidPlatform(this));
        }
        final Python py=Python.getInstance();
        PyObject pyobj=py.getModule("script");
        PyObject obj=pyobj.callAttr("hello");
        tv.setText(obj.toString());
    }
}