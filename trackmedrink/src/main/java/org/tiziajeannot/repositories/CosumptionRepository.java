package org.tiziajeannot.repositories;

import java.util.List;

import javax.enterprise.context.ApplicationScoped;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.transaction.Transactional;
import javax.ws.rs.WebApplicationException;

import org.tiziajeannot.entities.Consumption;

@ApplicationScoped
public class CosumptionRepository {
    @PersistenceContext
    private EntityManager entityManager;

    public List<Consumption> findAll() {
        return entityManager.createNamedQuery("Cosumptions.findAll", Consumption.class).getResultList();
    }

    public Consumption findById(Long id) {
        Consumption consumption = entityManager.find(Consumption.class, id);
        if (consumption == null) {
            throw new WebApplicationException("No activity with that id", 404);
        }
        return consumption;
    }

    @Transactional
    public void createConsumption(Consumption consumption) {
        entityManager.persist(consumption);
    }

    @Transactional
    public void deleteConsumption(Long id) {
        Consumption consumption = findById(id);
        entityManager.remove(consumption);
    }
}
