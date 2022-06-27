package org.tiziajeannot.endpoints;

import java.util.List;

import javax.enterprise.context.ApplicationScoped;
import javax.inject.Inject;
import javax.ws.rs.Consumes;
import javax.ws.rs.DELETE;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.PUT;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import org.tiziajeannot.entities.Activity;
import org.tiziajeannot.entities.Step;
import org.tiziajeannot.entities.User;
import org.tiziajeannot.repositories.ActivityRepository;
import org.tiziajeannot.repositories.UserRepository;
import org.tiziajeannot.requests.Activity.CreateActivity;
import org.tiziajeannot.requests.Activity.UpdateActivity;

@Path("activities")
@ApplicationScoped
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class ActivityEndpoint {
    @Inject ActivityRepository activityRepository;
    @Inject UserRepository userRepository;

    @POST
    public Response createActivity(CreateActivity request) {
        Activity activity = new Activity();
        User user = userRepository.findById(request.getUserID());
        user.addActivity(activity);
        activity.setName(request.getName());
        activity.setStart_time(request.getStart_time());
        activityRepository.createActivity(activity);
        return Response.ok().build();
    }

    @GET
    public Response getAll() {
        List<Activity> activities = activityRepository.findAll();
        return Response.ok(activities).build(); 
    }

    @GET
    @Path("/{id}")
    public Response getActivity(@PathParam("id") Long id) {
        Activity activity = activityRepository.findById(id);
        return Response.ok(activity).build();
    }

    @GET
    @Path("/{id}/steps")
    public Response getSteps(@PathParam("id") Long id) {
        try {
            Activity activity = activityRepository.findById(id);
            List<Step> steps = activity.getSteps();
            return Response.ok(steps).build();
        } catch (Exception e) {
           return Response.status(Response.Status.NOT_FOUND).build();
        }
    }

    @PUT
    @Path("/{id}")
    public Response updateActivity(@PathParam("id") Long id, UpdateActivity update) {
        activityRepository.updateActivity(id, update.getEnd_time());
        return Response.ok().build();
    }

    @DELETE
    @Path("/{id}")
    public Response deleteActivity(@PathParam("id") Long id) {
        activityRepository.DeleteActivity(id);
        return Response.status(204).build();
    }
}
