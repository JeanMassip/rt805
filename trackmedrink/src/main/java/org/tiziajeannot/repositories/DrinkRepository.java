package org.tiziajeannot.repositories;

import java.util.List;

import javax.enterprise.context.ApplicationScoped;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.transaction.Transactional;
import javax.ws.rs.WebApplicationException;

import org.tiziajeannot.entities.Drink;

@ApplicationScoped
public class DrinkRepository {
    @PersistenceContext
    private EntityManager entityManager;

    public List<Drink> findAll() {
        return entityManager.createNamedQuery("Drinks.findAll", Drink.class).getResultList();
    }

    public Drink findById(Long id) {
        Drink Drink = entityManager.find(Drink.class, id);
        if (Drink == null) {
            throw new WebApplicationException("No Drink with that id", 404);
        }
        return Drink;
    }

    @Transactional
    public void updateDrink(Long id, Float degree, String name) {
        Drink update = findById(id);
        update.setDegree(degree);
        update.setName(name);
    }

    @Transactional
    public void createDrink(Drink drink) {
        entityManager.persist(drink);
    }

    @Transactional
    public void DeleteDrink(Long id) {
        Drink d = findById(id);
        entityManager.remove(d);
    }
}
