package org.tiziajeannot.endpoints;

import java.util.List;

import javax.enterprise.context.ApplicationScoped;
import javax.inject.Inject;
import javax.websocket.server.PathParam;
import javax.ws.rs.Consumes;
import javax.ws.rs.DELETE;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import org.tiziajeannot.entities.Bar;
import org.tiziajeannot.entities.Consumption;
import org.tiziajeannot.entities.Step;
import org.tiziajeannot.repositories.StepRepository;

@Path("steps")
@ApplicationScoped
@Produces(MediaType.TEXT_XML)
@Consumes(MediaType.TEXT_XML)
public class StepEndpoints {
    @Inject StepRepository stepRepository;

    @POST
    public Response createActivity(Step step) {
        stepRepository.createStep(step);
        return Response.ok().build();
    }

    @GET
    @Path("/{id}")
    public Response getActivity(@PathParam("id") Long id) {
        Step step = stepRepository.findById(id);
        return Response.ok(step).build();
    }

    @GET
    @Path("/{id}/steps")
    public Response getSteps(@PathParam("id") Long id) {
        try {
            Step step = stepRepository.findById(id);
            List<Consumption> consumptions = step.getConsumptions();
            return Response.ok(consumptions).build();
        } catch (Exception e) {
           return Response.status(Response.Status.NOT_FOUND).build();
        }
    }

    @GET
    @Path("/{id}/bar")
    public Response getBar(@PathParam("id") Long id) {
        try {
            Step step = stepRepository.findById(id);
            Bar bar = step.getBar();
            return Response.ok(bar).build();
        } catch (Exception e) {
            return Response.status(Response.Status.NOT_FOUND).build();
        }
    }

    @DELETE
    @Path("/{id}")
    public Response deleteActivity(@PathParam("id") Long id) {
        stepRepository.DeleteStep(id);
        return Response.status(204).build();
    }
}
