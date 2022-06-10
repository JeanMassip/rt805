package org.tiziajeannot.repositories;

import java.util.List;

import javax.enterprise.context.ApplicationScoped;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.transaction.Transactional;
import javax.ws.rs.WebApplicationException;

import org.tiziajeannot.entities.Activity;

@ApplicationScoped
public class ActivityRepository {
    @PersistenceContext
    private EntityManager entityManager;

    public List<Activity> findAll() {
        return entityManager.createNamedQuery("Activities.findAll", Activity.class).getResultList();
    }

    public List<Activity> findByUserID(long id) {
        return entityManager.createQuery("qlString", Activity.class).getResultList();
    }

    public Activity findById(Long id) {
        Activity activity = entityManager.find(Activity.class, id);
        if (activity == null) {
            throw new WebApplicationException("No activity with that id", 404);
        }
        return activity;
    }

    @Transactional
    public void updateActivity(Long id, String end_time) {
        Activity update = findById(id);
        update.setEnd_time(end_time);
    }

    @Transactional
    public void createActivity(Activity activity) {
        entityManager.persist(activity);
    }

    @Transactional
    public void DeleteActivity(Long id) {
        Activity a = findById(id);
        entityManager.remove(a);
    }
}
