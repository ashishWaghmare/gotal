package com.ashish.gotal.metering;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

@Path("/metering")
public class MeteringController {

  @GET
  @Produces(MediaType.APPLICATION_JSON)
  public java.lang.String get() {
    return "Metering service";
  }
}
