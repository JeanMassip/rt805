package org.tiziajeannot.repositories;

import java.util.List;

import javax.enterprise.context.ApplicationScoped;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.transaction.Transactional;
import javax.ws.rs.WebApplicationException;

import org.tiziajeannot.entities.Bar;

@ApplicationScoped
public class BarRepository {
    @PersistenceContext
    private EntityManager entityManager;

    public List<Bar> findAll() {
        return entityManager.createNamedQuery("Bars.findAll", Bar.class).getResultList();
    }

    public Bar findById(Long id) {
        Bar activity = entityManager.find(Bar.class, id);
        if (activity == null) {
            throw new WebApplicationException("No activity with that id", 404);
        }
        return activity;
    }

    @Transactional
    public void updateBar(Long id, String name, Float position_lat, Float position_lon ) {
        Bar update = findById(id);
        update.setName(name);
        update.setPosition_lat(position_lat);
        update.setPosition_lon(position_lon);
    }

    @Transactional
    public void createBar(Bar bar) {
        entityManager.persist(bar);
    }

    @Transactional
    public void deleteBar(Long id) {
        Bar a = findById(id);
        entityManager.remove(a);
    }
} 