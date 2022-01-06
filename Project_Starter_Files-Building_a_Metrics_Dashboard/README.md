**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Please kindly check the 'answer-img' directory for all your required screenshots. *thanks*

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and 
include it here to verify the installation
##done
![metrics_dashboard](https://github.com/mordernGeek/CNAND_nd064_C4_Observability_Starter_Files/blob/master/answer-img/get%20all.PNG"get all")


## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.
##done 
![grafana_dashboard](https://github.com/mordernGeek/CNAND_nd064_C4_Observability_Starter_Files/blob/master/answer-img/grafana%20login%20dashboard.PNG "Grafana post-login")

## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.
##done
![Alt text](https://github.com/mordernGeek/CNAND_nd064_C4_Observability_Starter_Files/blob/master/answer-img/datasource%20prometheus%20metrics.PNG "a title")

## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.
#done
service level indicators are flags we put in place to identify if we meet the SLOs, so for 
monthly uptime - availability during specified month benchmarked against the SLO
request response time - latency of the server response benchmarked against the SLO

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 
#done
percentage uptime per month - availability
no of server downtimes in the month - cpu errors
latency rate per order -latency
total orders/requests per month - traffic
total fulfillment of orders per month


## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. 
Create a dashboard that show these values over a 24 hour period and take a screenshot.

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here. 
Also provide a (screenshot) sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.- 

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.
...
#i can't find my updated screenshot...
![jaeger](https://github.com/mordernGeek/CNAND_nd064_C4_Observability_Starter_Files/blob/master/answer-img/jaeger%20up%20and%20running.PNG "initial")


## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and 
to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.

![jaeger tracer span](https://github.com/mordernGeek/CNAND_nd064_C4_Observability_Starter_Files/blob/master/answer-img/python%20sample%20to%20span%20as%20requested.PNG "tracer_span?")

#i can't find my updated screenshot...

TROUBLE TICKET

Name: Damilola Banjoko

Date: 27/11/2021, updated!

Subject: SLI feedback

Affected Area: Uptime/ Availability

Severity: High

Description: 500 server errors means the server could not handle the request... should i call it a denial of service?
400 error could be an error from the client-end end or malicious attempt


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. 
Name four SLIs that you would use to measure the success of this SLO.
latency
traffic
saturation 
errors

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen.
 We will make a dashboard for this, but first write them down here.
ensure 99.95% uptime 
reduce latency by 5%
reduce network saturation by 25%

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. 
Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  

![my_first_dashboard](https://github.com/mordernGeek/CNAND_nd064_C4_Observability_Starter_Files/blob/master/answer-img/updating%20my%20new%20dashboard.PNG" KPIs")


total requests measures saturation by checking http requests
Latency measures delay/ load time
CPU Speed monitors performance thus availability