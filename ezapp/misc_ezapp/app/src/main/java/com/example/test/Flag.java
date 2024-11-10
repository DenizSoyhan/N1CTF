package com.example.test;

public class Flag {

    public String doGetValidFlag() {
        return "f";
    }

    public String getValidFlag(){
        return doGetValidFlag();
    }
}