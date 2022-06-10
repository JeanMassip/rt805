package org.tiziajeannot.repositories;

import java.util.List;

import javax.enterprise.context.ApplicationScoped;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.transaction.Transactional;
import javax.ws.rs.WebApplicationException;

import org.tiziajeannot.entities.Price;

@ApplicationScoped
public class PriceRepository {
    @PersistenceContext
    private EntityManager entityManager;

    public List<Price> findAll() {
        return entityManager.createNamedQuery("Activities.findAll", Price.class).getResultList();
    }

    public Price findById(Long id) {
        Price price = entityManager.find(Price.class, id);
        if (price == null) {
            throw new WebApplicationException("No Price with that id", 404);
        }
        return price;
    }

    @Transactional
    public void updatePrice(Long id, Integer price) {
        Price update = findById(id);
        update.setPrice(price);
    }

    @Transactional
    public void createPrice(Price price) {
        entityManager.persist(price);
    }

    @Transactional
    public void DeletePrice(Long id) {
        Price p = findById(id);
        entityManager.remove(p);
    }
}
