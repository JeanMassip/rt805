package org.tiziajeannot.requests;

import java.io.Serializable;

public class PriceUpdate implements Serializable {
    private int price;

    public int getPrice() {
        return this.price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

}
