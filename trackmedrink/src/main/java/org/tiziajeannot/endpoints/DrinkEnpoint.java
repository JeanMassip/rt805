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

import org.tiziajeannot.entities.Drink;
import org.tiziajeannot.repositories.DrinkRepository;

@Path("drinks")
@ApplicationScoped
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class DrinkEnpoint {
    @Inject DrinkRepository drinkRepository;

    @POST
    public Response createDrink(Drink drink) {
        drinkRepository.createDrink(drink);
        return Response.ok().build();
    }

    @GET
    public Response getDrinks() {
        List<Drink> drinks = drinkRepository.findAll();
        return Response.ok(drinks).build();
    }

    @GET
    @Path("/{id}")
    public Response getDrink(@PathParam("id") Long id) {
        Drink drink = drinkRepository.findById(id);
        return Response.ok(drink).build();
    }

    @DELETE
    @Path("/{id}")
    public Response deleteDrink(@PathParam("id") Long id) {
        drinkRepository.DeleteDrink(id);
        return Response.status(204).build();
    }
}

