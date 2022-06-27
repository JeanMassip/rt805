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
import org.tiziajeannot.repositories.BarRepository;

@Path("bars")
@ApplicationScoped
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class BarEndpoint {
    @Inject BarRepository barRepository;

    @POST
    public Response createBar(Bar bar) {
        barRepository.createBar(bar);
        return Response.ok().build();
    }

    @GET
    public Response getBars() {
        List<Bar> Bars = barRepository.findAll();
        return Response.ok(Bars).build();
    }

    @GET
    @Path("/{id}")
    public Response getBar(@PathParam("id") Long id) {
        Bar Bar = barRepository.findById(id);
        return Response.ok(Bar).build();
    }

    @DELETE
    @Path("/{id}")
    public Response deleteBar(@PathParam("id") Long id) {
        barRepository.deleteBar(id);
        return Response.status(204).build();
    }
}
