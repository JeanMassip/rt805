package org.tiziajeannot.entities;

import java.util.List;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.NamedQuery;
import javax.persistence.OneToMany;

@Entity
@NamedQuery(name = "Activities.findAll", query = "SELECT a FROM Activity a ORDER BY a.id")
public class Activity {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "id")
    private Long id;
    @Column(name = "name")
    private String name;
    @Column(name = "start_time")
    private String start_time;
    @Column(name = "end_time")
    private String end_time;
    @OneToMany(mappedBy = "activity")
    private transient List<Step> steps; 
    @ManyToOne
    @JoinColumn(name = "user_id")
    private User user;

    public Activity() {}

    public Long getId() {
        return this.id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getStart_time() {
        return this.start_time;
    }

    public void setStart_time(String start_time) {
        this.start_time = start_time;
    }

    public String getEnd_time() {
        return this.end_time;
    }

    public void setEnd_time(String end_time) {
        this.end_time = end_time;
    }

    public User getUser() {
        return this.user;
    }

    public void setUser(User user) {
        if (sameAsFormer(user)) {
            return ;
        }

        this.user = user;
        if (user!=null) {
            user.addActivity(this);
        }
    }

    private boolean sameAsFormer(User newUser) {
        return user==null? newUser == null : user.equals(newUser);
    }
    

    public List<Step> getSteps() {
        return this.steps;
    }

    public void setSteps(List<Step> steps) {
        this.steps = steps;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
