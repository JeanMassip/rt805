package org.tiziajeannot.endpoints;

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

import org.tiziajeannot.entities.Credentials;
import org.tiziajeannot.entities.User;
import org.tiziajeannot.repositories.UserRepository;

@Path("users")
@ApplicationScoped
@Produces(MediaType.TEXT_XML)
public class UserEndpoint {
    @Inject UserRepository userRepository;

    @POST
    @Consumes(MediaType.TEXT_XML)
    @Path("/register")
    public Response Register(User user) {
        userRepository.createUser(user);
        return Response.ok().build();
    }

    @POST
    @Consumes(MediaType.TEXT_XML)
    @Path("/sign-in")
    public Response SignIn(Credentials credentials) {
        User user = userRepository.findByEmail(credentials.getUsername());
        if (user.getPassword() != credentials.getPassword()) {
            return Response.status(Response.Status.FORBIDDEN).build();
        }
        return Response.ok(user).build();
    }

    @GET
    @Consumes(MediaType.TEXT_XML)
    @Path("/{id}/activities")
    public Response GetActivities(@PathParam("id") Long id) {
        try {
            User user = userRepository.findById(id);
            return Response.ok(user).build();
        } catch (Exception e) {
           return Response.status(Response.Status.NOT_FOUND).build();
        }
    }
}
