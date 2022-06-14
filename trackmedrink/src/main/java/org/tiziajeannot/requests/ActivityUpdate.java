package org.tiziajeannot.requests;

import java.io.Serializable;

public class ActivityUpdate implements Serializable {
    private String end_time;

    public String getEnd_time() {
        return this.end_time;
    }

    public void setEnd_time(String end_time) {
        this.end_time = end_time;
    }
    
}
