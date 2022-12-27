;; create the main project namespace
(ns weather-e-ink-display.core
  (:require [cljs-time.core :as time]
            [cljs-time.format :as fmt]
            [environ.boot :refer [environ]]))

;; enable cljs to print to the JS console of the browser
(enable-console-print!)
(println "Hello, World!")

(-> js/document
     (.getElementById "date")
     (.-innerHTML)
     (set! 
      (fmt/unparse 
       (fmt/formatter "HH:mm, EEEE, MMM dd") 
       (time/to-time-zone (time/time-zone-for-id "America/Montreal") (js/Date.)))))

(-> js/document
     (.getElementById "refresh-timestamp")
     (.-innerHTML)
     (set! 
      (fmt/unparse 
       (fmt/formatter "HH:mm") 
       (time/to-time-zone (time/time-zone-for-id "America/Montreal") (js/Date.)))))
