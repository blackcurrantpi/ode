{% assign data = include.data %}
<table class="asst-table" style="width: 100%;">
{% for exam in data.exams %}
<tr>
  <td style="width: 70%; vertical-align: top;">
      <table class="inner" style="width: 100%;">
        <tr>
            <td style="word-wrap: break-word; overflow-wrap: break-word; white-space: normal;">
                {{ exam.name }} &nbsp; &nbsp; {{ exam.date }}
            </td>
        </tr>
        {% if exam.info %}
        <tr>
            <td style="word-wrap: break-word; overflow-wrap: break-word; white-space: normal; max-width: 300px;">
                {{ exam.info }}
            </td>
        </tr>
        {% endif %}
        {% if exam.reviewguide %}
        <tr>
            <td><a href="{{ data.home }}/{{ exam.reviewguide }}">review guide</a></td>
        </tr>
        {% endif %}
        {% if exam.doc %}
        <tr>
            <td><a href="{{ data.home }}/{{ exam.doc }}">exam document</a></td>
        </tr>
        {% endif %}
        {% if exam.rubric %}
        <tr>
            <td><a href="{{ data.home }}/{{ exam.rubric }}">rubric</a></td>
        </tr>
        {% endif %}
      </table>
  </td>
  <td style="width: 30%; vertical-align: top;">
      <table class="inner" style="width: 100%;">
        {% if exam.blank %}
        <tr>
            <td><a href="{{ data.home }}/{{ exam.blank }}">practice exam (blank)</a></td>
        </tr>
        {% endif %}
        {% if exam.solutions %}
        <tr>
            <td><a href="{{ data.home }}/{{ exam.solutions }}">solutions</a></td>
        </tr>
        {% endif %}
      </table>
  </td>
</tr>
{% endfor %}
</table>
