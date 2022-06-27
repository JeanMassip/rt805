package org.tiziajeannot.repositories;

import java.util.List;

import javax.enterprise.context.ApplicationScoped;
import javax.persistence.EntityManager;
import javax.persistence.NoResultException;
import javax.persistence.NonUniqueResultException;
import javax.persistence.PersistenceContext;
import javax.persistence.TypedQuery;
import javax.transaction.Transactional;
import javax.ws.rs.WebApplicationException;

import org.tiziajeannot.entities.User;

@ApplicationScoped
public class UserRepository {
    @PersistenceContext
    private EntityManager entityManager;

    public List<User> findAll() {
        return entityManager.createNamedQuery("Users.findAll", User.class).getResultList();
    }

    public User findByEmail(String email) {
        try {
            TypedQuery<User> tq = entityManager.createQuery("SELECT u from User u WHERE email=?1", User.class);
            User result = tq.setParameter(1, email).getSingleResult();
            return result;
        } catch(NoResultException e) {
            throw new WebApplicationException("No user with that email", 404);
        } catch(NonUniqueResultException e) {
            throw new WebApplicationException("Something went REALLY wrong", 500);
        }
    }

    public User findById(Long id) {
        User user = entityManager.find(User.class, id);
        if (user == null) {
            throw new WebApplicationException("No User with that id", 404);
        }
        return user;
    }

    @Transactional
    public void updateUser(Long id, String email, String password) {
        User update = findById(id);
        update.setEmail(email);
        update.setPassword(password);
    }

    @Transactional
    public void createUser(User user) {
        entityManager.persist(user);
    }

    @Transactional
    public void DeleteUser(Long id) {
        User a = findById(id);
        entityManager.remove(a);
    }
}
