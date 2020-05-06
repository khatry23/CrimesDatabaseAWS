select n_killed, n_injured, offender_count, bias_desc
from dbapp.gun_violence g , dbapp.hatecrimes h
where g.state_name = h.state_name
and hyear = DATE_PART_YEAR(incident_date)

;
