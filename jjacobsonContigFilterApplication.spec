/*
A KBase module: jjacobsonContigFilterApplication
This sample module contains one small method that filters contigs.
*/

module jjacobsonContigFilterApplication {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_jjacobsonContigFilterApplication(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
