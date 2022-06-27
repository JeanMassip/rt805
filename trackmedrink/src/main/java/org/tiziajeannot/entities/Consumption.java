package org.tiziajeannot.entities;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.NamedQuery;

@Entity
@NamedQuery(name = "Consumptions.findAll", query = "SELECT c FROM Consumption c ORDER BY c.id")
public class Consumption {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "id")
    private Long id;
    @ManyToOne(optional = false, cascade = CascadeType.MERGE)
    @JoinColumn(name = "drink_id", referencedColumnName = "id")
    private Drink drink;
    @ManyToOne(optional = false, cascade = CascadeType.MERGE)
    @JoinColumn(name = "step_id", referencedColumnName = "id")
    private transient Step step;

    public Long getId() {
        return this.id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Drink getDrink() {
        return this.drink;
    }

    public void setDrink(Drink drink) {
        this.drink = drink;
    }

    public Step getStep() {
        return this.step;
    }

    public void setStep(Step step) {
        this.step = step;
    }

}
