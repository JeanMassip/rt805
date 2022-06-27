package org.tiziajeannot.endpoints;

import java.util.List;

import javax.enterprise.context.ApplicationScoped;
import javax.inject.Inject;
import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import org.tiziajeannot.entities.Activity;
import org.tiziajeannot.entities.User;
import org.tiziajeannot.repositories.ActivityRepository;
import org.tiziajeannot.repositories.UserRepository;
import org.tiziajeannot.requests.Credentials;

@Path("users")
@ApplicationScoped
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class UserEndpoint {
    @Inject UserRepository userRepository;
    @Inject ActivityRepository activityRepository;

    @POST
    @Path("/register")
    public Response Register(User user) {
        userRepository.createUser(user);
        return Response.ok().build();
    }

    @POST
    @Path("/sign-in")
    public Response SignIn(Credentials credentials) {
        User user = userRepository.findByEmail(credentials.getUsername());
        if (user.getPassword().equals(credentials.getPassword())) {
            return Response.ok(user).build();
        }
        return Response.status(Response.Status.FORBIDDEN).build();
    }

    @GET
    @Path("/{id}/activities")
    public Response GetActivities(@PathParam("id") Long id) {
        List<Activity> activities = activityRepository.findByUserID(id);
        return Response.ok(activities).build();
    }
}
