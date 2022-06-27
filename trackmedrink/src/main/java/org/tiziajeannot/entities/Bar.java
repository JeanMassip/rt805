package org.tiziajeannot.entities;

import java.util.List;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.NamedQuery;
import javax.persistence.OneToMany;

@Entity
@NamedQuery(name = "Bars.findAll", query = "SELECT b FROM Bar b ORDER BY b.id")
public class Bar {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "id")
    private Long id;
    @Column(name = "name")
    private String name;
    @Column(name = "position_lon")
    private Float position_lon;
    @Column(name = "position_lat")
    private Float position_lat;
    @OneToMany(mappedBy = "bar")
    private transient List<Step> steps;
    @OneToMany(mappedBy = "bar")
    private transient List<Price> prices;
    

    public Long getId() {
        return this.id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Float getPosition_lon() {
        return this.position_lon;
    }

    public void setPosition_lon(Float position_lon) {
        this.position_lon = position_lon;
    }

    public Float getPosition_lat() {
        return this.position_lat;
    }

    public void setPosition_lat(Float position_lat) {
        this.position_lat = position_lat;
    }

    public List<Step> getSteps() {
        return this.steps;
    }

    public void setSteps(List<Step> steps) {
        this.steps = steps;
    }

    public List<Price> getPrices() {
        return this.prices;
    }

    public void setPrices(List<Price> prices) {
        this.prices = prices;
    }
}
 