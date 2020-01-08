{% if prediction_success %}
import std.algorithm;
import std.conv;
import std.stdio;
import std.string;
{% endif %}
{% if mod or yes_str or no_str %}

{% endif %}
{% if mod %}
immutable long MOD = {{ mod }};
{% endif %}
{% if yes_str %}
immutable string YES = "{{ yes_str }}";
{% endif %}
{% if no_str %}
immutable string NO = "{{ no_str }}";
{% endif %}
{% if prediction_success %}

void solve({{ formal_arguments }}){

}

{% endif %}
// Generated by {{ atcodertools.version }} {{ atcodertools.url }}  (tips: You use the default template now. You can remove this line by using your custom template)
int main(){
    {% if prediction_success %}
    auto input = stdin.byLine.map!split.joiner;

    {{ input_part }}
    solve({{ actual_arguments }});
    {% else %}
    // Failed to predict input format
    {% endif %}
    return 0;
}
