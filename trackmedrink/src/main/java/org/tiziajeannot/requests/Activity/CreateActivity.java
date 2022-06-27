package org.tiziajeannot.requests.Activity;

import java.io.Serializable;

public class CreateActivity implements Serializable {
    private String start_time;
    private String name;
    private Long userID;

    public String getStart_time() {
        return this.start_time;
    }

    public void setStart_time(String start_time) {
        this.start_time = start_time;
    }

    public Long getUserID() {
        return this.userID;
    }

    public void setUserID(Long userID) {
        this.userID = userID;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
