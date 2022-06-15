package org.tiziajeannot.endpoints;

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

import org.tiziajeannot.entities.Consumption;
import org.tiziajeannot.repositories.ConsumptionRepository;

@Path("consumptions")
@ApplicationScoped
@Produces(MediaType.TEXT_XML)
@Consumes(MediaType.TEXT_XML)
public class ConsumptionsEndpoint {
    @Inject ConsumptionRepository consumptionRepository;

    @POST
    public Response createConsumption(Consumption consumption) {
        consumptionRepository.createConsumption(consumption);
        return Response.ok().build();
    }

    @GET
    @Path("/{id}")
    public Response getConsumption(@PathParam("id") Long id) {
        Consumption consumption = consumptionRepository.findById(id);
        return Response.ok(consumption).build();
    }

    @DELETE
    @Path("/{id}")
    public Response deleteConsumption(@PathParam("id") Long id) {
        consumptionRepository.deleteConsumption(id);
        return Response.status(204).build();
    }
}
