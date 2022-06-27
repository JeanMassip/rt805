package org.tiziajeannot.endpoints;

import java.util.List;

import javax.enterprise.context.ApplicationScoped;
import javax.inject.Inject;
import javax.websocket.server.PathParam;
import javax.ws.rs.Consumes;
import javax.ws.rs.DELETE;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.PUT;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import org.tiziajeannot.entities.Price;
import org.tiziajeannot.repositories.PriceRepository;
import org.tiziajeannot.requests.PriceUpdate;

@Path("prices")
@ApplicationScoped
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class PriceEndpoint {
    @Inject PriceRepository priceRepository;

    @POST
    public Response createPrice(Price price) {
        priceRepository.createPrice(price);
        return Response.ok().build();
    }

    @GET
    public Response getPrices() {
        List<Price> prices = priceRepository.findAll();
        return Response.ok(prices).build();
    }

    @GET
    @Path("/{id}")
    public Response getPrice(@PathParam("id") Long id) {
        Price price = priceRepository.findById(id);
        return Response.ok(price).build();
    }

    @PUT
    @Path("/{id}")
    public Response updatePrice(@PathParam("id") Long id, PriceUpdate update) {
        priceRepository.updatePrice(id, update.getPrice());
        return Response.ok().build();
    }

    @DELETE
    @Path("/{id}")
    public Response deletePrice(@PathParam("id") Long id) {
        priceRepository.DeletePrice(id);
        return Response.ok().build();
    }
}
