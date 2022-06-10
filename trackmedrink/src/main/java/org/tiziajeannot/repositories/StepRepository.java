package org.tiziajeannot.repositories;

import java.util.List;

import javax.enterprise.context.ApplicationScoped;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.transaction.Transactional;
import javax.ws.rs.WebApplicationException;

import org.tiziajeannot.entities.Step;

@ApplicationScoped
public class StepRepository {
    @PersistenceContext
    private EntityManager entityManager;

    public List<Step> findAll() {
        return entityManager.createNamedQuery("Activities.findAll", Step.class).getResultList();
    }

    public Step findById(Long id) {
        Step step = entityManager.find(Step.class, id);
        if (step == null) {
            throw new WebApplicationException("No Step with that id", 404);
        }
        return step;
    }

    @Transactional
    public void createStep(Step step) {
        entityManager.persist(step);
    }

    @Transactional
    public void DeleteStep(Long id) {
        Step a = findById(id);
        entityManager.remove(a);
    }
}
