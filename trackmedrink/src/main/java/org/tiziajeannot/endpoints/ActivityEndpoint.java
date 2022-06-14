package org.tiziajeannot.endpoints;

import java.util.List;

import javax.ejb.ApplicationException;
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
import org.tiziajeannot.repositories.ActivityRepository;
import org.tiziajeannot.requests.ActivityUpdate;

@Path("activities")
@ApplicationException
@Produces(MediaType.TEXT_XML)
@Consumes(MediaType.TEXT_XML)
public class ActivityEndpoint {
    @Inject ActivityRepository activityRepository;

    @POST
    public Response createActivity(Activity activity) {
        activityRepository.createActivity(activity);
        return Response.ok().build();
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
    public Response updateActivity(@PathParam("id") Long id, ActivityUpdate update) {
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
