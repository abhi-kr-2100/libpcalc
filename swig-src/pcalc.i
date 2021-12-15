%module pcalc
%{
#include "power-calculator/parser/parser.hpp"
#include "power-calculator/token/exceptions.hpp"
#include "power-calculator/parser/exceptions.hpp"
%}

%include <std_string.i>
%include <std_map.i>


namespace std {
    %template(VariablesTableType) map<string, double>;
}


class Parser
{
public:
    double evaluate(const std::string& expr) throw(
        Unknown_token, Bad_number, Runtime_error, Syntax_error);
    
    double evaluate(const std::string& expr,
        std::map<std::string, double>& variables_table);

    // the keyword used to introduce a new variable
    inline static const std::string var_declaration_key = "let";
private:
    std::map<std::string, double> variables_table;
    
    double variable_declaration(const Token_iter& s, const Token_iter& e,
        std::map<std::string, double>& variables_table);
    double assignment(const Token_iter& s, const Token_iter& e,
        std::map<std::string, double>& variables_table);
    double expression(const Token_iter& s, const Token_iter& e,
        std::map<std::string, double>& variables_table);
    double term(const Token_iter& s, const Token_iter& e,
        std::map<std::string, double>& variables_table);
    double exponent(const Token_iter& s, const Token_iter& e,
        std::map<std::string, double>& variables_table);
    double primary(const Token_iter& s, const Token_iter& e,
        std::map<std::string, double>& variables_table);
};
