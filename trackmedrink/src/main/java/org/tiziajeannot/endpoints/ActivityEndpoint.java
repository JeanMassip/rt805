package org.tiziajeannot.endpoints;

import javax.ejb.ApplicationException;
import javax.ws.rs.Consumes;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import org.tiziajeannot.entities.Activity;

@Path("activities")
@ApplicationException
@Produces(MediaType.TEXT_XML)
@Consumes(MediaType.TEXT_XML)
public class ActivityEndpoint {
    public Response createActivity(Activity activity) {}
    public Response getActivity(@PathParam("id") Long id) {}
    public Response updateActivity(Activity activity) {}
    public Response deleteActivity(@PathParam("id") Long id) {}
}
