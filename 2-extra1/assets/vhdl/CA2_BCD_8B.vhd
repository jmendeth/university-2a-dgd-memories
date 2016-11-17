library ieee;
use ieee.std_logic_1164.all;

entity CA2_BCD_8B is
  port ( CA2 : in std_logic_vector(7 downto 0);
         BCD : out std_logic_vector(7 downto 0) );
end;

architecture truth_table of CA2_BCD_8B is
begin
  with CA2 select
    BCD <= x"00" when x"00",
           x"01" when x"01",
           x"02" when x"02",
           x"03" when x"03",
           x"04" when x"04",
           x"05" when x"05",
           x"06" when x"06",
           x"07" when x"07",
           x"08" when x"08",
           x"09" when x"09",
           x"10" when x"0A",
           x"12" when x"0C",
           x"14" when x"0E",
           x"15" when x"0F",
           x"16" when x"10",
           x"18" when x"12",
           x"20" when x"14",
           x"21" when x"15",
           x"24" when x"18",
           x"25" when x"19",
           x"27" when x"1B",
           x"28" when x"1C",
           x"30" when x"1E",
           x"32" when x"20",
           x"35" when x"23",
           x"36" when x"24",
           x"40" when x"28",
           x"42" when x"2A",
           x"45" when x"2D",
           x"48" when x"30",
           x"49" when x"31",
           x"54" when x"36",
           x"56" when x"38",
           x"63" when x"3F",
           x"64" when x"40",
           x"72" when x"48",
           x"81" when x"51",
           "--------" when others;
end truth_table;
